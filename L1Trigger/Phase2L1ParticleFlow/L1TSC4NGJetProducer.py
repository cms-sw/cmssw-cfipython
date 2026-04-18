import FWCore.ParameterSet.Config as cms

def L1TSC4NGJetProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TSC4NGJetProducer',
    jets = cms.InputTag('l1tSC4PFL1PuppiExtendedEmulator'),
    doJEC = cms.bool(False),
    returnRawPt = cms.bool(False),
    correctorFile = cms.string(''),
    correctorDir = cms.string(''),
    l1tSC4NGJetModelPath = cms.string('L1TSC4NGJetModel_v0'),
    maxJets = cms.int32(16),
    nParticles = cms.int32(16),
    minPt = cms.double(10),
    maxEta = cms.double(2.4),
    classes = cms.vstring(
      'b',
      'c',
      'uds',
      'g',
      'tau_p',
      'tau_n',
      'mu',
      'e'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
