from System.Windows.Forms import Clipboard

import rhinoscriptsyntax as rs

__commandname__ = "GetDimValue"


def format_dim_values(dim_values):
  
  tmp_text = ""
  
  for i in xrange(len(dim_values)):
    
    v = str(dim_values[i])
    
    if i == 0:
      tmp_text = tmp_text + v
    else:
      tmp_text = tmp_text + "\n" + v
      
  return tmp_text


def objs_to_dim_value(objs):
  
  dim_values = []
  
  ### Get Block Name
  for obj in objs:
    
    if rs.IsDimension(obj):
      dim_values.append(rs.DimensionText(obj))
  
  ### Remove Duplicate
  dim_values_set = list(set(dim_values))
  
  ### Sorted
  dim_values_set_sorted = sorted(dim_values_set)
  
  return dim_values_set_sorted


def to_clipboad(dim_values):
    
    text_copy = format_dim_values(dim_values)
    Clipboard.SetText(text_copy)
    
    print(text_copy)


def RunCommand( is_interactive ):
  
  VERSION = "1.0.0.0"
  print("***RUN GetDimValue (ver {})".format(VERSION))
  
  objs = rs.SelectedObjects()
  
  ### Case A
  if len(objs) >= 1:
    
    dim_value_set = objs_to_dim_value(objs)
    if dim_value_set != []:
      to_clipboad(dim_value_set)

  ### Case B
  else:
    
    objs_new = rs.GetObjects(message="***Please Select Dimensions :")
    ### print(objs_new)
    
    ### to Ignore Case
    ###     - When processing is interrupted (Press ESC key)
    ###     - Not Selected
    
    if objs_new != None:
      dim_value_set = objs_to_dim_value(objs_new)
      if dim_value_set != []:
        to_clipboad(dim_value_set)
  
  
  
  # you can optionally return a value from this function
  # to signify command result. Return values that make
  # sense are
  #   0 == success
  #   1 == cancel
  # If this function does not return a value, success is assumed
  return 0
