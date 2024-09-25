import FWCore.ParameterSet.Config as cms

def PixelPopConDCSCablingAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PixelPopConDCSCablingAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
