import FWCore.ParameterSet.Config as cms

def AlignmentPrescaler(*args, **kwargs):
  mod = cms.EDProducer('AlignmentPrescaler',
    src = cms.InputTag('generalTracks'),
    assomap = cms.InputTag('OverlapAssoMap'),
    PrescFileName = cms.string('PrescaleFactors.root'),
    PrescTreeName = cms.string('AlignmentHitMap'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
