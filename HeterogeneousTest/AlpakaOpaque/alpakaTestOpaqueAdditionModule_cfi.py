import FWCore.ParameterSet.Config as cms

alpakaTestOpaqueAdditionModule = cms.EDAnalyzer('AlpakaTestOpaqueAdditionModule@alpaka',
  size = cms.uint32(1048576),
  alpaka = cms.untracked.PSet(),
  mightGet = cms.optional.untracked.vstring
)
