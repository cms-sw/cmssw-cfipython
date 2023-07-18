import FWCore.ParameterSet.Config as cms

gemRecHitFlatTableProducer = cms.EDProducer('GEMRecHitFlatTableProducer',
  name = cms.required.string,
  doc = cms.string(''),
  extension = cms.bool(False),
  skipNonExistingSrc = cms.bool(False),
  src = cms.required.InputTag,
  variables = cms.PSet(),
  detIdVariables = cms.PSet(),
  globalPosVariables = cms.PSet(),
  mightGet = cms.optional.untracked.vstring
)
