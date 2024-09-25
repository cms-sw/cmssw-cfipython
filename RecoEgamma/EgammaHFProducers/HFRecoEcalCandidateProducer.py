import FWCore.ParameterSet.Config as cms

def HFRecoEcalCandidateProducer(*args, **kwargs):
  mod = cms.EDProducer('HFRecoEcalCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
