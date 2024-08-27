import FWCore.ParameterSet.Config as cms

def AlignmentPrescaler(**kwargs):
  mod = cms.EDProducer('AlignmentPrescaler',
    src = cms.InputTag('generalTracks'),
    assomap = cms.InputTag('OverlapAssoMap'),
    PrescFileName = cms.string('PrescaleFactors.root'),
    PrescTreeName = cms.string('AlignmentHitMap'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
