import FWCore.ParameterSet.Config as cms

hcalTopologyIdealBase = cms.ESProducer('HcalTopologyIdealEP',
  Exclude = cms.untracked.string(''),
  MergePosition = cms.untracked.bool(False),
  appendToDataLabel = cms.string('')
)
