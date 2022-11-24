import FWCore.ParameterSet.Config as cms

checkBPHWriteDecay = cms.EDAnalyzer('CheckBPHWriteDecay',
  candsLabel = cms.vstring(),
  runNumber = cms.uint32(0),
  evtNumber = cms.uint32(0),
  fileName = cms.untracked.string(''),
  writePtr = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
