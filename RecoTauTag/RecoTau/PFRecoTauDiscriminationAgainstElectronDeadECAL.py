import FWCore.ParameterSet.Config as cms

def PFRecoTauDiscriminationAgainstElectronDeadECAL(*args, **kwargs):
  mod = cms.EDProducer('PFRecoTauDiscriminationAgainstElectronDeadECAL',
    dR = cms.double(0.08),
    minStatus = cms.uint32(12),
    extrapolateToECalEntrance = cms.bool(True),
    verbosity = cms.int32(0),
    PFTauProducer = cms.InputTag('fixme'),
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('AND'),
      leadTrack = cms.PSet(
        cut = cms.double(0),
        Producer = cms.InputTag('fixme')
      ),
      decayMode = cms.PSet(
        cut = cms.double(0),
        Producer = cms.InputTag('fixme')
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
