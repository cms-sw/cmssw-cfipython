import FWCore.ParameterSet.Config as cms

isolEcalPixelTrackFilter = cms.EDFilter('HLTEcalPixelIsolTrackFilter',
  saveTags = cms.bool(True),
  candTag = cms.InputTag('hltIsolEcalPixelTrackProd'),
  MaxEnergyIn = cms.double(1.2),
  MaxEnergyOut = cms.double(1.2),
  NMaxTrackCandidates = cms.int32(10),
  DropMultiL2Event = cms.bool(False)
)
