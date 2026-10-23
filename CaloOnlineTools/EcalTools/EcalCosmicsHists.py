import FWCore.ParameterSet.Config as cms

def EcalCosmicsHists(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalCosmicsHists',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
