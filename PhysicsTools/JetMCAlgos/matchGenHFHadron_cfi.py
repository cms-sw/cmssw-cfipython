import FWCore.ParameterSet.Config as cms

matchGenHFHadron = cms.EDProducer('GenHFHadronMatcher',
  genParticles = cms.required.InputTag,
  jetFlavourInfos = cms.required.InputTag,
  noBBbarResonances = cms.bool(True),
  onlyJetClusteredHadrons = cms.bool(False),
  flavour = cms.int32(5),
  mightGet = cms.optional.untracked.vstring
)
