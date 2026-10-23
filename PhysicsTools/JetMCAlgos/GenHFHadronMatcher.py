import FWCore.ParameterSet.Config as cms

def GenHFHadronMatcher(*args, **kwargs):
  mod = cms.EDProducer('GenHFHadronMatcher',
    genParticles = cms.required.InputTag,
    jetFlavourInfos = cms.required.InputTag,
    noBBbarResonances = cms.bool(True),
    onlyJetClusteredHadrons = cms.bool(False),
    flavour = cms.int32(5),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
