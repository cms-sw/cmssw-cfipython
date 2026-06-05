import FWCore.ParameterSet.Config as cms

def GctDigiToPsbText(*args, **kwargs):
  mod = cms.EDAnalyzer('GctDigiToPsbText',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
