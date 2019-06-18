import FWCore.ParameterSet.Config as cms

lheInfoTable = cms.EDProducer('LHETablesProducer',
  lheInfo = cms.VInputTag(
    'externalLHEProducer',
    'source'
  ),
  precision = cms.int32(-1),
  storeLHEParticles = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
