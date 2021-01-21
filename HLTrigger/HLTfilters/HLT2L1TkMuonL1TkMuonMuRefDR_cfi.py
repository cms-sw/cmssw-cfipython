import FWCore.ParameterSet.Config as cms

HLT2L1TkMuonL1TkMuonMuRefDR = cms.EDFilter('HLT2L1TkMuonL1TkMuonMuRefDR',
  saveTags = cms.bool(True),
  originTag1 = cms.VInputTag('hltOriginal1'),
  originTag2 = cms.VInputTag('hltOriginal2'),
  inputTag1 = cms.InputTag('hltFiltered1'),
  inputTag2 = cms.InputTag('hltFiltered2'),
  MinDR = cms.double(-1),
  MinN = cms.int32(1),
  mightGet = cms.optional.untracked.vstring
)
