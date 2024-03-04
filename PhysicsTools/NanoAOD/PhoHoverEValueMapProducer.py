import FWCore.ParameterSet.Config as cms

def PhoHoverEValueMapProducer(**kwargs):
  mod = cms.EDProducer('PhoHoverEValueMapProducer',
    src = cms.required.InputTag,
    relative = cms.required.bool,
    QuadraticEAFile_HoverE = cms.required.FileInPath,
    rho = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
