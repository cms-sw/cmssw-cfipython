import FWCore.ParameterSet.Config as cms

def HLTGenValSource(**kwargs):
  mod = cms.EDProducer('HLTGenValSource',
    objType = cms.required.string,
    hltPathsToCheck = cms.required.vstring,
    dqmDirName = cms.string('HLTGenVal'),
    hltProcessName = cms.string('HLT'),
    dR2limit = cms.double(0.1),
    doOnlyLastFilter = cms.bool(False),
    inputCollections = cms.PSet(
      genParticles = cms.InputTag('genParticles'),
      genMET = cms.InputTag('genMetTrue'),
      ak4GenJets = cms.InputTag('ak4GenJets'),
      ak8GenJets = cms.InputTag('ak8GenJets'),
      TrigEvent = cms.InputTag('hltTriggerSummaryAOD')
    ),
    histConfigs = cms.VPSet(
      cms.PSet(
        binLowEdges = cms.vdouble(
          0,
          5,
          10,
          12.5,
          15,
          17.5,
          20,
          22.5,
          25,
          30,
          35,
          40,
          45,
          50,
          60,
          80,
          100,
          150,
          200,
          250,
          300,
          350,
          400
        ),
        vsVar = cms.string('pt')
      ),
      cms.PSet(
        binLowEdges = cms.vdouble(
          -10,
          -8,
          -6,
          -5,
          -4,
          -3,
          -2,
          -1,
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          8,
          10
        ),
        vsVar = cms.string('eta')
      )
    ),
    histConfigs2D = cms.VPSet(
      cms.PSet(
        binLowEdgesX = cms.vdouble(
          0,
          5,
          10,
          12.5,
          15,
          17.5,
          20,
          22.5,
          25,
          30,
          35,
          40,
          45,
          50,
          60,
          80,
          100,
          150,
          200,
          250,
          300,
          350,
          400
        ),
        binLowEdgesY = cms.vdouble(
          -10,
          -8,
          -6,
          -5,
          -4,
          -3,
          -2,
          -1,
          0,
          1,
          2,
          3,
          4,
          5,
          6,
          8,
          10
        ),
        vsVarX = cms.string('pt'),
        vsVarY = cms.string('eta')
      )
    ),
    binnings = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
