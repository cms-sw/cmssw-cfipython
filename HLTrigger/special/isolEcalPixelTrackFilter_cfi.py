import FWCore.ParameterSet.Config as cms

isolEcalPixelTrackFilter = cms.EDFilter('HLTEcalPixelIsolTrackFilter',
  saveTags = cms.bool(True),
  candTag = cms.InputTag('hltIsolEcalPixelTrackProd'),
  MaxEnergyInEB = cms.double(2),
  MaxEnergyInEE = cms.double(4),
  MaxEnergyOutEB = cms.double(1.2),
  MaxEnergyOutEE = cms.double(2),
  NMaxTrackCandidates = cms.int32(10),
  DropMultiL2Event = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
