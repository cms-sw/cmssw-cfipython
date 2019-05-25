import FWCore.ParameterSet.Config as cms

muonRefPatCount = cms.EDFilter('MuonRefPatCount',
  src = cms.InputTag(''),
  cut = cms.string(''),
  minNumber = cms.uint32(0)
)
