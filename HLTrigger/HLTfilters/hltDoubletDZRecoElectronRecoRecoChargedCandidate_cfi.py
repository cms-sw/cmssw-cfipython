import FWCore.ParameterSet.Config as cms

hltDoubletDZRecoElectronRecoRecoChargedCandidate = cms.EDFilter('HLT2ElectronMuonDZ',
  saveTags = cms.bool(False),
  originTag1 = cms.VInputTag('hltOriginal1'),
  originTag2 = cms.VInputTag('hltOriginal2'),
  inputTag1 = cms.InputTag('hltFiltered1'),
  inputTag2 = cms.InputTag('hltFiltered2'),
  triggerType1 = cms.int32(0),
  triggerType2 = cms.int32(0),
  MinDR = cms.double(-1),
  MaxDZ = cms.double(0.2),
  checkSC = cms.bool(False),
  MinN = cms.int32(1)
)
