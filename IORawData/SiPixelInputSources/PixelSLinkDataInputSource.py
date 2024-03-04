import FWCore.ParameterSet.Config as cms

def PixelSLinkDataInputSource(**kwargs):
  mod = cms.Source('PixelSLinkDataInputSource')
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
