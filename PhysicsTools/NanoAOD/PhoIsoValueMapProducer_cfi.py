import FWCore.ParameterSet.Config as cms

PhoIsoValueMapProducer = cms.EDProducer('PhoIsoValueMapProducer',
  src = cms.required.InputTag,
  relative = cms.required.bool,
  mapIsoChg = cms.required.InputTag,
  mapIsoNeu = cms.required.InputTag,
  mapIsoPho = cms.required.InputTag,
  EAFile_PFIso_Chg = cms.required.FileInPath,
  EAFile_PFIso_Neu = cms.required.FileInPath,
  EAFile_PFIso_Pho = cms.required.FileInPath,
  rho_PFIso = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
