import FWCore.ParameterSet.Config as cms

def PixelPopConFEDCablingAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelPopConFEDCablingAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
