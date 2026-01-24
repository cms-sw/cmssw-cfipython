import FWCore.ParameterSet.Config as cms

def MPIController(*args, **kwargs):
  mod = cms.EDProducer('MPIController',
    mode = cms.untracked.string('CommWorld'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
