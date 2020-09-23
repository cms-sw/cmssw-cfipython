import FWCore.ParameterSet.Config as cms

genWeightsTable = cms.EDProducer('GenWeightsTableProducer',
  genEvent = cms.InputTag('generator'),
  genLumiInfoHeader = cms.InputTag('generator'),
  lheInfo = cms.VInputTag(
    'externalLHEProducer',
    'source'
  ),
  preferredPDFs = cms.VPSet(
  ),
  namedWeightIDs = cms.required.vstring,
  namedWeightLabels = cms.required.vstring,
  lheWeightPrecision = cms.required.int32,
  maxPdfWeights = cms.required.uint32,
  keepAllPSWeights = cms.required.bool,
  debug = cms.optional.untracked.bool,
  mightGet = cms.optional.untracked.vstring
)
