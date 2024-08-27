import FWCore.ParameterSet.Config as cms

def ShiftedParticleMETcorrInputProducer(**kwargs):
  mod = cms.EDProducer('ShiftedParticleMETcorrInputProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
