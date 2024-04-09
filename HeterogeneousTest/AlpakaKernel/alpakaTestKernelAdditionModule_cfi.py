import FWCore.ParameterSet.Config as cms

alpakaTestKernelAdditionModule = cms.EDAnalyzer('AlpakaTestKernelAdditionModule@alpaka',
  size = cms.uint32(1048576),
  alpaka = cms.untracked.PSet(),
  mightGet = cms.optional.untracked.vstring
)
