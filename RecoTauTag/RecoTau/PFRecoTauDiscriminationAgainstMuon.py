import FWCore.ParameterSet.Config as cms

def PFRecoTauDiscriminationAgainstMuon(*args, **kwargs):
  mod = cms.EDProducer('PFRecoTauDiscriminationAgainstMuon',
    a = cms.double(0.5),
    c = cms.double(0),
    b = cms.double(0.5),
    PFTauProducer = cms.InputTag('pfRecoTauProducer'),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('and'),
      leadTrack = cms.PSet(
        cut = cms.required.double,
        Producer = cms.required.InputTag
      )
    ),
    discriminatorOption = cms.string('noSegMatch'),
    HoPMin = cms.double(0.2),
    maxNumberOfMatches = cms.int32(0),
    checkNumMatches = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
