import FWCore.ParameterSet.Config as cms

lheInfoTable = cms.EDProducer('LHETablesProducer',
  lheInfo = cms.InputTag('externalLHEProducer'),
  precision = cms.int32(-1),
  storeLHEParticles = cms.bool(False)
)
