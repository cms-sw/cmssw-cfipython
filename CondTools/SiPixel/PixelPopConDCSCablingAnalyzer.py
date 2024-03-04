import FWCore.ParameterSet.Config as cms

def PixelPopConDCSCablingAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PixelPopConDCSCablingAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
