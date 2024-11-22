import FWCore.ParameterSet.Config as cms

def ShiftedPFJetProducer(*args, **kwargs):
  mod = cms.EDProducer('ShiftedPFJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
