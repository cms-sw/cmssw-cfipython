import FWCore.ParameterSet.Config as cms

def BetaStarPackedCandidateVarProducer(**kwargs):
  mod = cms.EDProducer('BetaStarPackedCandidateVarProducer',
    srcJet = cms.required.InputTag,
    srcPF = cms.required.InputTag,
    maxDR = cms.required.double,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
