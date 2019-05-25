import FWCore.ParameterSet.Config as cms

ptMinGsfElectronCountFilter = cms.EDFilter('PtMinGsfElectronCountFilter',
  src = cms.InputTag(''),
  ptMin = cms.double(0),
  minNumber = cms.uint32(0)
)
