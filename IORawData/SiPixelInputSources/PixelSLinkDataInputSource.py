import FWCore.ParameterSet.Config as cms

def PixelSLinkDataInputSource(*args, **kwargs):
  mod = cms.Source('PixelSLinkDataInputSource')
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
