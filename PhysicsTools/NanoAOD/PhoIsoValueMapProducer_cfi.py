import FWCore.ParameterSet.Config as cms

PhoIsoValueMapProducer = cms.EDProducer('PhoIsoValueMapProducer',
  src = cms.required.InputTag,
  relative = cms.required.bool,
  doQuadratic = cms.bool(False),
  mapIsoChg = cms.optional.InputTag,
  mapIsoNeu = cms.optional.InputTag,
  mapIsoPho = cms.optional.InputTag,
  EAFile_PFIso_Chg = cms.optional.FileInPath,
  EAFile_PFIso_Neu = cms.optional.FileInPath,
  EAFile_PFIso_Pho = cms.optional.FileInPath,
  rho_PFIso = cms.required.InputTag,
  QuadraticEAFile_PFIso_Chg = cms.optional.FileInPath,
  QuadraticEAFile_PFIso_ECal = cms.optional.FileInPath,
  QuadraticEAFile_PFIso_HCal = cms.optional.FileInPath,
  mightGet = cms.optional.untracked.vstring
)
