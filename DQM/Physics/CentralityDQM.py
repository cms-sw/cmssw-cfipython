import FWCore.ParameterSet.Config as cms

def CentralityDQM(*args, **kwargs):
  mod = cms.EDProducer('CentralityDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
