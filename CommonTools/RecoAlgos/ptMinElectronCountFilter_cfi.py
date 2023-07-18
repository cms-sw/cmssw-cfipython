import FWCore.ParameterSet.Config as cms

ptMinElectronCountFilter = cms.EDFilter('PtMinElectronCountFilter',
  src = cms.InputTag(''),
  ptMin = cms.double(0),
  minNumber = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)
