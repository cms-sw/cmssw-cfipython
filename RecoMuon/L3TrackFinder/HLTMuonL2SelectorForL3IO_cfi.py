import FWCore.ParameterSet.Config as cms

HLTMuonL2SelectorForL3IO = cms.EDProducer('HLTMuonL2SelectorForL3IO',
  l2Src = cms.InputTag('hltL2Muons', 'UpdatedAtVtx'),
  l3OISrc = cms.InputTag('hltL2Muons', 'UpdatedAtVtx'),
  useOuterHitPosition = cms.bool(True),
  xDiffMax = cms.double(0.5),
  yDiffMax = cms.double(0.5),
  zDiffMax = cms.double(9999),
  dRDiffMax = cms.double(0.01)
)
