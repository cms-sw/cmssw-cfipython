import FWCore.ParameterSet.Config as cms

def EcalSimRawData(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalSimRawData',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
