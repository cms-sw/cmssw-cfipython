import FWCore.ParameterSet.Config as cms

def BetaStarPackedCandidateVarProducer(*args, **kwargs):
  mod = cms.EDProducer('BetaStarPackedCandidateVarProducer',
    srcJet = cms.required.InputTag,
    srcPF = cms.required.InputTag,
    maxDR = cms.required.double,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
