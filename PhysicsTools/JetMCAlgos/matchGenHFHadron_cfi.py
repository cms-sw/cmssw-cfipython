import FWCore.ParameterSet.Config as cms

matchGenHFHadron = cms.EDProducer('GenHFHadronMatcher',
  noBBbarResonances = cms.bool(True),
  onlyJetClusteredHadrons = cms.bool(False),
  flavour = cms.int32(5)
)
