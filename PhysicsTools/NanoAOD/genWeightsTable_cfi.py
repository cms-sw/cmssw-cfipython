import FWCore.ParameterSet.Config as cms

genWeightsTable = cms.EDProducer('GenWeightsTableProducer',
  genEvent = cms.InputTag('generator'),
  genLumiInfoHeader = cms.InputTag('generator'),
  lheInfo = cms.VInputTag(
    'externalLHEProducer',
    'source'
  ),
  preferredPDFs = cms.VPSet(
  )
)
