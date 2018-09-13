import FWCore.ParameterSet.Config as cms

hcalTopologyIdeal = cms.ESProducer('HcalTopologyIdealEP',
  Exclude = cms.untracked.string(''),
  hcalTopologyConstants = cms.PSet(
    mode = cms.string('HcalTopologyMode::LHC'),
    maxDepthHB = cms.int32(2),
    maxDepthHE = cms.int32(3)
  ),
  appendToDataLabel = cms.string('')
)
