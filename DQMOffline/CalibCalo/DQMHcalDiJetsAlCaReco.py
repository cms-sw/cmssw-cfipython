import FWCore.ParameterSet.Config as cms

def DQMHcalDiJetsAlCaReco(*args, **kwargs):
  mod = cms.EDProducer('DQMHcalDiJetsAlCaReco',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
