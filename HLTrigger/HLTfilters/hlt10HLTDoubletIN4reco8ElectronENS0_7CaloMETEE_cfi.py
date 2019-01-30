import FWCore.ParameterSet.Config as cms

hlt10HLTDoubletIN4reco8ElectronENS0_7CaloMETEE = cms.EDFilter('HLT2ElectronCaloMET',
  saveTags = cms.bool(False),
  originTag1 = cms.VInputTag('hltOriginal1'),
  originTag2 = cms.VInputTag('hltOriginal2'),
  inputTag1 = cms.InputTag('hltFiltered1'),
  inputTag2 = cms.InputTag('hltFiltered22'),
  triggerType1 = cms.int32(0),
  triggerType2 = cms.int32(0),
  MinDphi = cms.double(1),
  MaxDphi = cms.double(-1),
  MinDeta = cms.double(1),
  MaxDeta = cms.double(-1),
  MinMinv = cms.double(1),
  MaxMinv = cms.double(-1),
  MinDelR = cms.double(1),
  MaxDelR = cms.double(-1),
  MinPt = cms.double(1),
  MaxPt = cms.double(-1),
  MinN = cms.int32(1)
)
