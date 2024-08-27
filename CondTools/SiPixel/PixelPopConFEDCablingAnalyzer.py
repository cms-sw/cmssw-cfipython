import FWCore.ParameterSet.Config as cms

def PixelPopConFEDCablingAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PixelPopConFEDCablingAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
