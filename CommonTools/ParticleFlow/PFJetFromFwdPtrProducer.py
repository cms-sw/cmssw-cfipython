import FWCore.ParameterSet.Config as cms

def PFJetFromFwdPtrProducer(*args, **kwargs):
  mod = cms.EDProducer('PFJetFromFwdPtrProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
