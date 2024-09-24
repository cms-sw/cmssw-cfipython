import FWCore.ParameterSet.Config as cms

def BPHWriteSpecificDecay(**kwargs):
  mod = cms.EDProducer('BPHWriteSpecificDecay',
    pVertexLabel = cms.string(''),
    patMuonLabel = cms.string(''),
    ccCandsLabel = cms.string(''),
    pfCandsLabel = cms.string(''),
    pcCandsLabel = cms.string(''),
    gpCandsLabel = cms.string(''),
    k0CandsLabel = cms.string(''),
    l0CandsLabel = cms.string(''),
    kSCandsLabel = cms.string(''),
    lSCandsLabel = cms.string(''),
    oniaName = cms.string('oniaCand'),
    sdName = cms.string('kx0Cand'),
    ssName = cms.string('phiCand'),
    buName = cms.string('buFitted'),
    bpName = cms.string('bpFitted'),
    bdName = cms.string('bdFitted'),
    bsName = cms.string('bsFitted'),
    k0Name = cms.string('k0Fitted'),
    l0Name = cms.string('l0Fitted'),
    b0Name = cms.string('b0Fitted'),
    lbName = cms.string('lbFitted'),
    bcName = cms.string('bcFitted'),
    psi2SName = cms.string('psi2SFitted'),
    x3872Name = cms.string('x3872Fitted'),
    writeVertex = cms.bool(True),
    writeMomentum = cms.bool(True),
    recoSelect = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod