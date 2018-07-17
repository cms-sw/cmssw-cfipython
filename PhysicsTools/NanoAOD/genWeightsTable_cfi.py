import FWCore.ParameterSet.Config as cms

genWeightsTable = cms.EDProducer('GenWeightsTableProducer',
  genEvent = cms.InputTag('generator'),
  lheInfo = cms.InputTag('externalLHEProducer'),
  preferredPDFs = cms.VPSet(
  )
)
