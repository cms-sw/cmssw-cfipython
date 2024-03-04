import FWCore.ParameterSet.Config as cms

def HFRecoEcalCandidateProducer(**kwargs):
  mod = cms.EDProducer('HFRecoEcalCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
