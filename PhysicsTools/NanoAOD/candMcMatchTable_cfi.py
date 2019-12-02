import FWCore.ParameterSet.Config as cms

candMcMatchTable = cms.EDProducer('CandMCMatchTableProducer',
  objName = cms.required.string,
  branchName = cms.required.string,
  docString = cms.required.string,
  src = cms.required.InputTag,
  mcMap = cms.required.InputTag,
  objType = cms.required.string,
  mcMapVisTau = cms.optional.InputTag,
  mightGet = cms.optional.untracked.vstring
)
